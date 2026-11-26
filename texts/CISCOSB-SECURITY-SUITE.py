#
# PySNMP MIB module CISCOSB-SECURITY-SUITE (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCOSB-SECURITY-SUITE
# Produced by pysmi-1.1.12 at Thu Nov 26 06:07:45 2026
# On host runnervm0hi8g platform Linux version 7.0.0-1020-azure by user runner
# Using Python version 3.13.18 (main, Oct 26 2026, 14:19:33) [GCC 15.2.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
switch001, Percents = mibBuilder.importSymbols("CISCOSB-MIB", "switch001", "Percents")
InterfaceIndex, InterfaceIndexOrZero, ifIndex = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex", "InterfaceIndexOrZero", "ifIndex")
PortList, = mibBuilder.importSymbols("Q-BRIDGE-MIB", "PortList")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, ModuleIdentity, TimeTicks, MibIdentifier, iso, Counter32, IpAddress, Integer32, NotificationType, ObjectIdentity, Unsigned32, Bits, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "ModuleIdentity", "TimeTicks", "MibIdentifier", "iso", "Counter32", "IpAddress", "Integer32", "NotificationType", "ObjectIdentity", "Unsigned32", "Bits", "Gauge32")
RowStatus, DisplayString, TruthValue, TextualConvention, RowPointer = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "DisplayString", "TruthValue", "TextualConvention", "RowPointer")
rlSecuritySuiteMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 120))
rlSecuritySuiteMib.setRevisions(('2006-01-09 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: rlSecuritySuiteMib.setRevisionsDescriptions(('Add per port dos attack table suport\n                rlSecuritySuiteDenyTypesTable ,rlSecuritySuiteDoSSynAttackTable.',))
if mibBuilder.loadTexts: rlSecuritySuiteMib.setLastUpdated('200604080000Z')
if mibBuilder.loadTexts: rlSecuritySuiteMib.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: rlSecuritySuiteMib.setContactInfo('Postal: 170 West Tasman Drive\n        San Jose , CA 95134-1706\n        USA\n\n        \n        Website:  Cisco Small Business Support Community <http://www.cisco.com/go/smallbizsupport>')
if mibBuilder.loadTexts: rlSecuritySuiteMib.setDescription('The private MIB module definition for blocking attacks\n                such as DoS(=Denial Of Service), SYN and well known viruses Attacks\n                in CISCOSB devices.')
class RlsecuritySuiteGlobalEnableType(TextualConvention, Integer32):
    description = 'Specifies the operating modes of the security-suite'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("enable-global-rules-only", 1), ("enable-all-rules-types", 2), ("disable", 3), ("enable-interface-rules-only", 4))

class RlSecuritySuiteKnownDosAttackType(TextualConvention, Integer32):
    description = 'Specifies well-known DoS attack'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("stacheldraht", 1), ("invasor-Trojan", 2), ("back-orifice-Trojan", 3))

class RlSecuritySuiteKnownDosAttackProtocolType(TextualConvention, Integer32):
    description = 'Specifies protocol type of the well-known DoS attack'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("tcp", 1), ("upd", 2))

class RlSecuritySuiteAllMartianEntryType(TextualConvention, Integer32):
    description = 'Specifies Martian-address origin: pre-defined (reserved) or statically configured'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("reserved", 1), ("static", 2))

class RlSecuritySuiteDenyAttackType(TextualConvention, Integer32):
    description = 'Specifies the deny attack types'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("syn", 1), ("icmp-echo-request", 2), ("fragmented", 3))

class RlSecuritySuiteDenySynFinTcp(TextualConvention, Integer32):
    description = 'Specifies the dropping SYN, FIN flags enabled TCP packets status'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("deny", 1), ("permit", 2))

class RlSecuritySuiteSynProtectionMode(TextualConvention, Integer32):
    description = 'Specifies the TCP SYN attack protection mode .'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("disabled", 1), ("report", 2), ("block", 3))

class RlSecuritySuiteSynProtectionPortMode(TextualConvention, Integer32):
    description = 'Specifies the TCP SYN attack protection mode .'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("normal", 1), ("attacked", 2), ("blocked", 3))

rlSecuritySuiteGlobalEnable = MibScalar((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 120, 1), RlsecuritySuiteGlobalEnableType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlSecuritySuiteGlobalEnable.setStatus('current')
if mibBuilder.loadTexts: rlSecuritySuiteGlobalEnable.setDescription('This scalar globally enables/disables the DoS attack Suite. ')
rlSecuritySuiteKnownDoSAttacksTable = MibTable((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 120, 2), )
if mibBuilder.loadTexts: rlSecuritySuiteKnownDoSAttacksTable.setStatus('current')
if mibBuilder.loadTexts: rlSecuritySuiteKnownDoSAttacksTable.setDescription('This table enables/disable well-know DoS attacks,\n        applied globally to all ifIndexes.')
rlSecuritySuiteKnownDoSAttacksEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 120, 2, 1), ).setIndexNames((0, "CISCOSB-SECURITY-SUITE", "rlSecuritySuiteKnownDoSAttack"))
if mibBuilder.loadTexts: rlSecuritySuiteKnownDoSAttacksEntry.setStatus('current')
if mibBuilder.loadTexts: rlSecuritySuiteKnownDoSAttacksEntry.setDescription('Each entry in this table describes one well known DoS attack address')
rlSecuritySuiteKnownDoSAttack = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 120, 2, 1, 1), RlSecuritySuiteKnownDosAttackType())
if mibBuilder.loadTexts: rlSecuritySuiteKnownDoSAttack.setStatus('current')
if mibBuilder.loadTexts: rlSecuritySuiteKnownDoSAttack.setDescription('A well-known DoS attack to enable')
rlSecuritySuiteKnownDoSAttackEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 120, 2, 1, 2), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlSecuritySuiteKnownDoSAttackEnable.setStatus('current')
if mibBuilder.loadTexts: rlSecuritySuiteKnownDoSAttackEnable.setDescription('Enable/Disable a well-known DoS attack ')
rlSecuritySuiteKnownDoSAttacksDetailsTable = MibTable((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 120, 3), )
if mibBuilder.loadTexts: rlSecuritySuiteKnownDoSAttacksDetailsTable.setStatus('current')
if mibBuilder.loadTexts: rlSecuritySuiteKnownDoSAttacksDetailsTable.setDescription('This read-only table used to present the detailed attributes\n        of each well-known DoS attack. Used for presentation propose only.')
rlSecuritySuiteKnownDoSAttacksDetailsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 120, 3, 1), ).setIndexNames((0, "CISCOSB-SECURITY-SUITE", "rlSecuritySuiteKnownDoSAttack"))
if mibBuilder.loadTexts: rlSecuritySuiteKnownDoSAttacksDetailsEntry.setStatus('current')
if mibBuilder.loadTexts: rlSecuritySuiteKnownDoSAttacksDetailsEntry.setDescription('Each entry in this table describes one well known DoS attack address ,')
rlSecuritySuiteKnownDoSAttackProtocl = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 120, 3, 1, 1), RlSecuritySuiteKnownDosAttackProtocolType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlSecuritySuiteKnownDoSAttackProtocl.setStatus('current')
if mibBuilder.loadTexts: rlSecuritySuiteKnownDoSAttackProtocl.setDescription('Specifies the protocol type of the relevant well-known attack')
rlSecuritySuiteKnownDoSAttackSrcTcpUdpPort = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 120, 3, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlSecuritySuiteKnownDoSAttackSrcTcpUdpPort.setStatus('current')
if mibBuilder.loadTexts: rlSecuritySuiteKnownDoSAttackSrcTcpUdpPort.setDescription('Specifies the source tcp/udp port of the relevant well-known attack')
rlSecuritySuiteKnownDoSAttackDestTcpUdpPort = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 120, 3, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlSecuritySuiteKnownDoSAttackDestTcpUdpPort.setStatus('current')
if mibBuilder.loadTexts: rlSecuritySuiteKnownDoSAttackDestTcpUdpPort.setDescription('Specifies the destination tcp/udp port of the relevant well-known attack')
rlSecuritySuiteReservedMartianAddresses = MibScalar((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 120, 4), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlSecuritySuiteReservedMartianAddresses.setStatus('current')
if mibBuilder.loadTexts: rlSecuritySuiteReservedMartianAddresses.setDescription("This scalar globally enables/disables discarding of the IP\n     well-known addresses described below:\n    -------------------------------------------------------------------------------\n    |  Address block               |  Present use\n    |-------------------------------------------------------------------------------\n    |0.0.0.0/8                     |  Addresses in this block refer to source hosts\n    |(except 0.0.0.0/32            |  on 'this' network.\n    | as source address)           |\n    |------------------------------------------------------------------------------\n    |127.0.0.0/8                   | This block is assigned for use as the Internet host loop-back address.\n    |-----------------------------------------------------------------------------------------------------\n    |192.0.2.0/24                  | This block is assigned as 'TEST-NET'\n    |                              | for use in documentation and example code.\n    |---------------------------------------------------------------------------\n    |224.0.0.0/4 as source.        | This block, formerly known as the Class D address space,\n    |                              | is allocated for use in IPv4 multicast address assignments.\n    |-------------------------------------------------------------------------------------------\n    |240.0.0.0/4                   |\n    |(except 255.255.255.255/32    | This block, formerly known as the Class E address space, is reserved.\n    | as destination address)      |\n    |-------------------------------------------------------------------------------------------------------\n   ")
rlSecuritySuiteMartianAddrAllTable = MibTable((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 120, 5), )
if mibBuilder.loadTexts: rlSecuritySuiteMartianAddrAllTable.setStatus('current')
if mibBuilder.loadTexts: rlSecuritySuiteMartianAddrAllTable.setDescription('This read-only table specifies all current configured Martian addresses -\n        both pre-defined (=reserved) and used-configured (=static) addresses')
rlSecuritySuiteMartianAddrAllEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 120, 5, 1), ).setIndexNames((0, "CISCOSB-SECURITY-SUITE", "rlSecuritySuiteMartianAddr"), (0, "CISCOSB-SECURITY-SUITE", "rlSecuritySuiteMartianAddrNetMask"))
if mibBuilder.loadTexts: rlSecuritySuiteMartianAddrAllEntry.setStatus('current')
if mibBuilder.loadTexts: rlSecuritySuiteMartianAddrAllEntry.setDescription('Each entry in this table describes one Martian address ,\n   packets with this address as IP source or IP destination, are discarded.')
rlSecuritySuiteMartianAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 120, 5, 1, 1), IpAddress())
if mibBuilder.loadTexts: rlSecuritySuiteMartianAddr.setStatus('current')
if mibBuilder.loadTexts: rlSecuritySuiteMartianAddr.setDescription('An IP address to discard all packets with that address as source\n        or destination')
rlSecuritySuiteMartianAddrNetMask = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 120, 5, 1, 2), IpAddress())
if mibBuilder.loadTexts: rlSecuritySuiteMartianAddrNetMask.setStatus('current')
if mibBuilder.loadTexts: rlSecuritySuiteMartianAddrNetMask.setDescription('Specify the net mask that comprise the destination IP address prefix.')
rlSecuritySuiteAllMartianEntryType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 120, 5, 1, 3), RlSecuritySuiteAllMartianEntryType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlSecuritySuiteAllMartianEntryType.setStatus('current')
if mibBuilder.loadTexts: rlSecuritySuiteAllMartianEntryType.setDescription('Specific the entry origin: pre-defined (reserved) of statically configured.')
rlSecuritySuiteMartianAddrTable = MibTable((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 120, 6), )
if mibBuilder.loadTexts: rlSecuritySuiteMartianAddrTable.setStatus('current')
if mibBuilder.loadTexts: rlSecuritySuiteMartianAddrTable.setDescription('This table specifies the Martian addresses -\n        the addresses that packets with these IP addressed as source or\n        destination are discarded.')
rlSecuritySuiteMartianAddrEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 120, 6, 1), ).setIndexNames((0, "CISCOSB-SECURITY-SUITE", "rlSecuritySuiteMartianAddr"), (0, "CISCOSB-SECURITY-SUITE", "rlSecuritySuiteMartianAddrNetMask"))
if mibBuilder.loadTexts: rlSecuritySuiteMartianAddrEntry.setStatus('current')
if mibBuilder.loadTexts: rlSecuritySuiteMartianAddrEntry.setDescription('Each entry in this table describes one Martian address ,\n   packets with this address as IP source or IP destination, are discarded.')
rlSecuritySuiteMartianAddrStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 120, 6, 1, 1), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rlSecuritySuiteMartianAddrStatus.setStatus('current')
if mibBuilder.loadTexts: rlSecuritySuiteMartianAddrStatus.setDescription('The status of a table entry.\n        It is used to delete/Add an entry from this table.')
rlSecuritySuiteDoSSynAttackTable = MibTable((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 120, 7), )
if mibBuilder.loadTexts: rlSecuritySuiteDoSSynAttackTable.setStatus('current')
if mibBuilder.loadTexts: rlSecuritySuiteDoSSynAttackTable.setDescription('This table contains IP address and rate, to limit DoS SYN attacks from\n        a specific IP address and interface(s)')
rlSecuritySuiteDoSSynAttackEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 120, 7, 1), ).setIndexNames((0, "CISCOSB-SECURITY-SUITE", "rlSecuritySuiteDoSSynAttackIfIndex"), (0, "CISCOSB-SECURITY-SUITE", "rlSecuritySuiteDoSSynAttackAddr"), (0, "CISCOSB-SECURITY-SUITE", "rlSecuritySuiteDoSSynAttackNetMask"))
if mibBuilder.loadTexts: rlSecuritySuiteDoSSynAttackEntry.setStatus('current')
if mibBuilder.loadTexts: rlSecuritySuiteDoSSynAttackEntry.setDescription('Each entry in this table describes one Martian address ,\n   packets with this address as IP source or IP destination, are discarded.')
rlSecuritySuiteDoSSynAttackIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 120, 7, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: rlSecuritySuiteDoSSynAttackIfIndex.setStatus('current')
if mibBuilder.loadTexts: rlSecuritySuiteDoSSynAttackIfIndex.setDescription('Interface which the attack is applied on')
rlSecuritySuiteDoSSynAttackAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 120, 7, 1, 2), IpAddress())
if mibBuilder.loadTexts: rlSecuritySuiteDoSSynAttackAddr.setStatus('current')
if mibBuilder.loadTexts: rlSecuritySuiteDoSSynAttackAddr.setDescription('An IP address to discard all packets with that address as destination')
rlSecuritySuiteDoSSynAttackNetMask = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 120, 7, 1, 3), IpAddress())
if mibBuilder.loadTexts: rlSecuritySuiteDoSSynAttackNetMask.setStatus('current')
if mibBuilder.loadTexts: rlSecuritySuiteDoSSynAttackNetMask.setDescription('Relevant when rlSecuritySuiteSynAttackRangeType equals prefix(2).\n        Specify the number of bits that comprise the destination\n        IP address prefix.')
rlSecuritySuiteDoSSynAttackSynRate = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 120, 7, 1, 4), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rlSecuritySuiteDoSSynAttackSynRate.setStatus('current')
if mibBuilder.loadTexts: rlSecuritySuiteDoSSynAttackSynRate.setDescription('Specify the maximum connections per second allowed from this IP address\n        and rlSecuritySuiteSynAttackPortList')
rlSecuritySuiteDoSSynAttackStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 120, 7, 1, 6), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rlSecuritySuiteDoSSynAttackStatus.setStatus('current')
if mibBuilder.loadTexts: rlSecuritySuiteDoSSynAttackStatus.setDescription('The status of a table entry.\n        It is used to delete/Add an entry from this table.')
rlSecuritySuiteDenyTypesTable = MibTable((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 120, 8), )
if mibBuilder.loadTexts: rlSecuritySuiteDenyTypesTable.setStatus('current')
if mibBuilder.loadTexts: rlSecuritySuiteDenyTypesTable.setDescription('This table specifies the ip address and TCP ports that\n        TCP SYN packets from them on a specific interfaces are dropped.')
rlSecuritySuiteDenyTypesEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 120, 8, 1), ).setIndexNames((0, "CISCOSB-SECURITY-SUITE", "rlSecuritySuiteDenyIfIndex"), (0, "CISCOSB-SECURITY-SUITE", "rlSecuritySuiteDenyAttackType"), (0, "CISCOSB-SECURITY-SUITE", "rlSecuritySuiteDenyDestAddr"), (0, "CISCOSB-SECURITY-SUITE", "rlSecuritySuiteDenyNetMask"), (0, "CISCOSB-SECURITY-SUITE", "rlSecuritySuiteDenyDestPort"))
if mibBuilder.loadTexts: rlSecuritySuiteDenyTypesEntry.setStatus('current')
if mibBuilder.loadTexts: rlSecuritySuiteDenyTypesEntry.setDescription('Each entry in this table describes one ip address, TCP port and\n   list of ifIndexes, that packets with these attributes are discarded.')
rlSecuritySuiteDenyIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 120, 8, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: rlSecuritySuiteDenyIfIndex.setStatus('current')
if mibBuilder.loadTexts: rlSecuritySuiteDenyIfIndex.setDescription('Interface which the attack is applied on')
rlSecuritySuiteDenyAttackType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 120, 8, 1, 2), RlSecuritySuiteDenyAttackType())
if mibBuilder.loadTexts: rlSecuritySuiteDenyAttackType.setStatus('current')
if mibBuilder.loadTexts: rlSecuritySuiteDenyAttackType.setDescription('The specific deny attack type')
rlSecuritySuiteDenyDestAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 120, 8, 1, 3), IpAddress())
if mibBuilder.loadTexts: rlSecuritySuiteDenyDestAddr.setStatus('current')
if mibBuilder.loadTexts: rlSecuritySuiteDenyDestAddr.setDescription('An IP address to discard all packets with that address as destination')
rlSecuritySuiteDenyNetMask = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 120, 8, 1, 4), IpAddress())
if mibBuilder.loadTexts: rlSecuritySuiteDenyNetMask.setStatus('current')
if mibBuilder.loadTexts: rlSecuritySuiteDenyNetMask.setDescription('Relevant when rlSecuritySuiteDenyTCPRangeType equals mask(1).\n        Specify the number of bits that comprise the destination\n        IP address prefix.')
rlSecuritySuiteDenyDestPort = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 120, 8, 1, 5), Integer32())
if mibBuilder.loadTexts: rlSecuritySuiteDenyDestPort.setStatus('current')
if mibBuilder.loadTexts: rlSecuritySuiteDenyDestPort.setDescription('Destination TCP port.\n        Use 65553 to specify all ports.\n        This key-field is relevant in specific attack types (not all)\n        Use 0 when not relevant.')
rlSecuritySuiteDenyStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 120, 8, 1, 6), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rlSecuritySuiteDenyStatus.setStatus('current')
if mibBuilder.loadTexts: rlSecuritySuiteDenyStatus.setDescription('The status of a table entry.\n        It is used to delete/Add an entry from this table.')
rlSecuritySuiteDenySynFinTcp = MibScalar((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 120, 9), RlSecuritySuiteDenySynFinTcp()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlSecuritySuiteDenySynFinTcp.setStatus('current')
if mibBuilder.loadTexts: rlSecuritySuiteDenySynFinTcp.setDescription('This scalar globally enable or disable dropping of tcp packets with both SYN and FIN flags enabled. ')
rlSecuritySuiteSynProtectionMode = MibScalar((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 120, 10), RlSecuritySuiteSynProtectionMode()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlSecuritySuiteSynProtectionMode.setStatus('current')
if mibBuilder.loadTexts: rlSecuritySuiteSynProtectionMode.setDescription("This scalar globally set protection mode on TCP SYN traffic.\n      Disabled - the system doesn't support protection against TCP SYN attack.\n      Report   - the system doesn't support protection against TCP SYN attack,but reports about it.\n      Block    - the systems supports protection against TCP SYN attack by blocking this traffic on the port.  ")
rlSecuritySuiteSynProtectionTreshold = MibScalar((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 120, 11), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlSecuritySuiteSynProtectionTreshold.setStatus('current')
if mibBuilder.loadTexts: rlSecuritySuiteSynProtectionTreshold.setDescription('This scalar globally set protection mode treshold value in packet per second\n      on TCP SYN traffic.')
rlSecuritySuiteSynProtectionRecoveryTimeout = MibScalar((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 120, 12), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlSecuritySuiteSynProtectionRecoveryTimeout.setStatus('current')
if mibBuilder.loadTexts: rlSecuritySuiteSynProtectionRecoveryTimeout.setDescription('This scalar globally set protection reovery time out in secounds.')
rlSecuritySuiteSynProtectionPortTable = MibTable((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 120, 13), )
if mibBuilder.loadTexts: rlSecuritySuiteSynProtectionPortTable.setStatus('current')
if mibBuilder.loadTexts: rlSecuritySuiteSynProtectionPortTable.setDescription('This table keeps SYN protection status per port.')
rlSecuritySuiteSynProtectionPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 120, 13, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: rlSecuritySuiteSynProtectionPortEntry.setStatus('current')
if mibBuilder.loadTexts: rlSecuritySuiteSynProtectionPortEntry.setDescription('Each entry in this table describes TCP SYN protection status for one port.')
rlSecuritySuiteSynProtectionPortMode = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 120, 13, 1, 1), RlSecuritySuiteSynProtectionPortMode()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlSecuritySuiteSynProtectionPortMode.setStatus('current')
if mibBuilder.loadTexts: rlSecuritySuiteSynProtectionPortMode.setDescription("The port's TCP SYN protection mode.")
rlSecuritySuiteSynProtectionPortModeLastTimeAttack = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 120, 13, 1, 2), RlSecuritySuiteSynProtectionPortMode()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlSecuritySuiteSynProtectionPortModeLastTimeAttack.setStatus('current')
if mibBuilder.loadTexts: rlSecuritySuiteSynProtectionPortModeLastTimeAttack.setDescription("The port's TCP SYN protection last attack time mode.")
rlSecuritySuiteSynProtectionPortLastTimeAttack = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 120, 13, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlSecuritySuiteSynProtectionPortLastTimeAttack.setStatus('current')
if mibBuilder.loadTexts: rlSecuritySuiteSynProtectionPortLastTimeAttack.setDescription("The port's TCP SYN protection last attack time.")
mibBuilder.exportSymbols("CISCOSB-SECURITY-SUITE", rlSecuritySuiteSynProtectionPortModeLastTimeAttack=rlSecuritySuiteSynProtectionPortModeLastTimeAttack, rlSecuritySuiteGlobalEnable=rlSecuritySuiteGlobalEnable, rlSecuritySuiteKnownDoSAttacksDetailsEntry=rlSecuritySuiteKnownDoSAttacksDetailsEntry, rlSecuritySuiteMartianAddrTable=rlSecuritySuiteMartianAddrTable, rlSecuritySuiteSynProtectionPortEntry=rlSecuritySuiteSynProtectionPortEntry, rlSecuritySuiteKnownDoSAttacksEntry=rlSecuritySuiteKnownDoSAttacksEntry, rlSecuritySuiteMartianAddrAllTable=rlSecuritySuiteMartianAddrAllTable, rlSecuritySuiteSynProtectionPortLastTimeAttack=rlSecuritySuiteSynProtectionPortLastTimeAttack, rlSecuritySuiteMib=rlSecuritySuiteMib, rlSecuritySuiteSynProtectionPortMode=rlSecuritySuiteSynProtectionPortMode, rlSecuritySuiteAllMartianEntryType=rlSecuritySuiteAllMartianEntryType, rlSecuritySuiteDenyAttackType=rlSecuritySuiteDenyAttackType, rlSecuritySuiteDenyStatus=rlSecuritySuiteDenyStatus, rlSecuritySuiteMartianAddrAllEntry=rlSecuritySuiteMartianAddrAllEntry, RlSecuritySuiteSynProtectionMode=RlSecuritySuiteSynProtectionMode, rlSecuritySuiteDenyIfIndex=rlSecuritySuiteDenyIfIndex, rlSecuritySuiteDoSSynAttackAddr=rlSecuritySuiteDoSSynAttackAddr, RlsecuritySuiteGlobalEnableType=RlsecuritySuiteGlobalEnableType, RlSecuritySuiteAllMartianEntryType=RlSecuritySuiteAllMartianEntryType, RlSecuritySuiteKnownDosAttackType=RlSecuritySuiteKnownDosAttackType, rlSecuritySuiteDoSSynAttackIfIndex=rlSecuritySuiteDoSSynAttackIfIndex, rlSecuritySuiteDoSSynAttackTable=rlSecuritySuiteDoSSynAttackTable, rlSecuritySuiteDenySynFinTcp=rlSecuritySuiteDenySynFinTcp, rlSecuritySuiteDenyTypesTable=rlSecuritySuiteDenyTypesTable, rlSecuritySuiteKnownDoSAttackDestTcpUdpPort=rlSecuritySuiteKnownDoSAttackDestTcpUdpPort, rlSecuritySuiteDenyTypesEntry=rlSecuritySuiteDenyTypesEntry, RlSecuritySuiteDenyAttackType=RlSecuritySuiteDenyAttackType, rlSecuritySuiteKnownDoSAttackSrcTcpUdpPort=rlSecuritySuiteKnownDoSAttackSrcTcpUdpPort, rlSecuritySuiteSynProtectionPortTable=rlSecuritySuiteSynProtectionPortTable, rlSecuritySuiteDoSSynAttackEntry=rlSecuritySuiteDoSSynAttackEntry, PYSNMP_MODULE_ID=rlSecuritySuiteMib, rlSecuritySuiteKnownDoSAttacksTable=rlSecuritySuiteKnownDoSAttacksTable, rlSecuritySuiteDenyDestAddr=rlSecuritySuiteDenyDestAddr, rlSecuritySuiteMartianAddrStatus=rlSecuritySuiteMartianAddrStatus, rlSecuritySuiteKnownDoSAttackEnable=rlSecuritySuiteKnownDoSAttackEnable, rlSecuritySuiteMartianAddr=rlSecuritySuiteMartianAddr, RlSecuritySuiteDenySynFinTcp=RlSecuritySuiteDenySynFinTcp, rlSecuritySuiteDoSSynAttackNetMask=rlSecuritySuiteDoSSynAttackNetMask, rlSecuritySuiteSynProtectionTreshold=rlSecuritySuiteSynProtectionTreshold, rlSecuritySuiteDoSSynAttackStatus=rlSecuritySuiteDoSSynAttackStatus, rlSecuritySuiteKnownDoSAttack=rlSecuritySuiteKnownDoSAttack, RlSecuritySuiteKnownDosAttackProtocolType=RlSecuritySuiteKnownDosAttackProtocolType, rlSecuritySuiteMartianAddrNetMask=rlSecuritySuiteMartianAddrNetMask, RlSecuritySuiteSynProtectionPortMode=RlSecuritySuiteSynProtectionPortMode, rlSecuritySuiteKnownDoSAttacksDetailsTable=rlSecuritySuiteKnownDoSAttacksDetailsTable, rlSecuritySuiteDoSSynAttackSynRate=rlSecuritySuiteDoSSynAttackSynRate, rlSecuritySuiteReservedMartianAddresses=rlSecuritySuiteReservedMartianAddresses, rlSecuritySuiteDenyNetMask=rlSecuritySuiteDenyNetMask, rlSecuritySuiteSynProtectionMode=rlSecuritySuiteSynProtectionMode, rlSecuritySuiteKnownDoSAttackProtocl=rlSecuritySuiteKnownDoSAttackProtocl, rlSecuritySuiteMartianAddrEntry=rlSecuritySuiteMartianAddrEntry, rlSecuritySuiteDenyDestPort=rlSecuritySuiteDenyDestPort, rlSecuritySuiteSynProtectionRecoveryTimeout=rlSecuritySuiteSynProtectionRecoveryTimeout)
