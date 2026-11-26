#
# PySNMP MIB module CISCO-HARDWARE-IP-VERIFY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-HARDWARE-IP-VERIFY-MIB
# Produced by pysmi-1.1.12 at Thu Nov 26 06:07:46 2026
# On host runnervm0hi8g platform Linux version 7.0.0-1020-azure by user runner
# Using Python version 3.13.18 (main, Oct 26 2026, 14:19:33) [GCC 15.2.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, ModuleIdentity, TimeTicks, MibIdentifier, iso, Counter32, IpAddress, Integer32, NotificationType, ObjectIdentity, Unsigned32, Bits, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "ModuleIdentity", "TimeTicks", "MibIdentifier", "iso", "Counter32", "IpAddress", "Integer32", "NotificationType", "ObjectIdentity", "Unsigned32", "Bits", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ciscoHardwareIpVerifyMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 804))
ciscoHardwareIpVerifyMIB.setRevisions(('2012-09-04 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoHardwareIpVerifyMIB.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoHardwareIpVerifyMIB.setLastUpdated('201209040000Z')
if mibBuilder.loadTexts: ciscoHardwareIpVerifyMIB.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoHardwareIpVerifyMIB.setContactInfo('Cisco Systems\n            Customer Service\n\n            Postal: 170 W Tasman Drive\n            San Jose, CA  95134\n            USA\n\n            Tel: +1 800 553-NETS\n\n            E-mail: cs-lan-switch-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoHardwareIpVerifyMIB.setDescription("This MIB module defines management objects for\n        configuration and monitoring of the Intrusion \n        Detection System (IDS) that checks for IP packet\n        verification. \n\n        The following terms are used throughout the MIB:\n            IDS:  Intrusion Detection System\n            CRC:  Cyclic Redundancy Check\n             DF:  Don't Fragment\n        ")
ciscoHardwareIpVerifyMIBNotifs = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 804, 0))
ciscoHardwareIpVerifyMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 804, 1))
ciscoHardwareIpVerifyMIBConform = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 804, 2))
chivIpVerifyTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 804, 1, 1), )
if mibBuilder.loadTexts: chivIpVerifyTable.setStatus('current')
if mibBuilder.loadTexts: chivIpVerifyTable.setDescription('A list of IDS check configuration and statistical information \n        for each IP type and each IDS check type on the management\n        device.')
chivIpVerifyEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 804, 1, 1, 1), ).setIndexNames((0, "CISCO-HARDWARE-IP-VERIFY-MIB", "chivIpVerifyCheckIpType"), (0, "CISCO-HARDWARE-IP-VERIFY-MIB", "chivIpVerifyCheckTypeName"))
if mibBuilder.loadTexts: chivIpVerifyEntry.setStatus('current')
if mibBuilder.loadTexts: chivIpVerifyEntry.setDescription('An entry contains the IDS packet check configuration \n        information and the associated counters.')
chivIpVerifyCheckIpType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 804, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("ipv4", 1), ("ipv6", 2))))
if mibBuilder.loadTexts: chivIpVerifyCheckIpType.setStatus('current')
if mibBuilder.loadTexts: chivIpVerifyCheckIpType.setDescription('This object indicates the IP address type for \n        IDS packet check.')
chivIpVerifyCheckTypeName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 804, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17))).clone(namedValues=NamedValues(("addressSrcBroadcast", 1), ("addressSrcMulticast", 2), ("addressDestZero", 3), ("addressIdentical", 4), ("addressSrcReserved", 5), ("addressClassE", 6), ("checksum", 7), ("protocol", 8), ("fragment", 9), ("lengthMinimum", 10), ("lengthConsistent", 11), ("lengthMaximumFragment", 12), ("lengthMaximumUdp", 13), ("lengthMaximumTcp", 14), ("tcpFlags", 15), ("tcpTinyFlags", 16), ("version", 17))))
if mibBuilder.loadTexts: chivIpVerifyCheckTypeName.setStatus('current')
if mibBuilder.loadTexts: chivIpVerifyCheckTypeName.setDescription('This object indicates the IDS packet check type\n        which can be configured on the device. Each check type\n        is a specific criteria. Those IP packets \n        that matches the certain criteria are dropped. \n\n            addressSrcBroadcast(1)\n                Drop the IPv4 packet if the source \n                address is a broadcast IPv4 address.\n\n            addressSrcMulticast(2)\n                Drop the IPv4 packet if the source \n                address is a multicast IPv4 address.\n\n            addressDestZero(3)\n                Drop the IPv4 packet if the destination \n                address is 0.0.0.0.\n\n            addressIdentical(4)\n                Drop the IPv4 packet if the source IPv4 \n                address is identical to destination IPv4 \n                address.\n\n            addressSrcReserved(5)\n                Drop the IPv4 packet if the source address \n                is a reserved IPv4 address.\n\n            addressClassE(6)\n                Drop the IPv4 packet if either the source \n                address or destination address is a class E \n                IPv4 address.\n\n            checksum(7)\n                Drops the IPv4 packet if its checksum is invalid.\n\n            protocol(8)\n                Drop the IPv4 packet if the packet fragment \n                has an invalid IP protocol number\n\n            fragment(9)\n                Drop the IPv4 packet if the packet fragment \n                has a nonzero offset and the DF bit is active.\n\n            lengthMinimum(10)\n                Drop the IPv4 packet if the Ethernet frame \n                length is less than the IP packet length plus \n                four octets (the CRC length).\n\n            lengthConsistent(11)\n                Drop the IPv4 or IPv6 packet where the Ethernet \n                frame size is greater than or equal to the IP packet \n                length plus the Ethernet header.\n\n            lengthMaximumFragment(12)\n                Drop the IPv4 or IPv6 packet if the maximum \n                fragment offset is greater than 65536.\n\n            lengthMaximumUdp(13)\n                Drop the IPv4 or IPv6 packet if the IP payload \n                length is less than the UDP packet length.\n\n            lengthMaximumTcp(14)\n                Drop the IPv4 or IPv6 packet if the TCP length \n                is greater than the IP payload length.\n\n            tcpFlags(15)\n                Drop the IPv4 packet if verification of TCP \n                packet header fails.\n\n            tcpTinyFlags(16)\n                Drop the IPv4 or IPv6 packet if the IP fragment \n                offset is 1, or if the IP fragment offset is 0 \n                and the IP payload length is less than 16.\n\n            version(17)\n                Drop the IPv4 packet if the Ethertype is not \n                set to 4 (IPv4); and drops the IPv6 packet if \n                the Ethertype is not set to 6 (IPv6).')
chivIpVerifyCheckStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 804, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disabled", 1), ("enabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: chivIpVerifyCheckStatus.setStatus('current')
if mibBuilder.loadTexts: chivIpVerifyCheckStatus.setDescription('This object specifies the IDS packet check configuration\n        status.')
chivIpVerifyPacketsDropped = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 804, 1, 1, 1, 4), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: chivIpVerifyPacketsDropped.setStatus('current')
if mibBuilder.loadTexts: chivIpVerifyPacketsDropped.setDescription('This object indicates the number of packets which has\n        been dropped.')
ciscoHardwareIpVerifyMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 804, 2, 1))
ciscoHardwareIpVerifyMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 804, 2, 2))
ciscoHardwareIpVerifyMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 804, 2, 1, 1)).setObjects(("CISCO-HARDWARE-IP-VERIFY-MIB", "ciscoHardwareIpVerifyMIBStatisticGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoHardwareIpVerifyMIBCompliance = ciscoHardwareIpVerifyMIBCompliance.setStatus('current')
if mibBuilder.loadTexts: ciscoHardwareIpVerifyMIBCompliance.setDescription('The compliance statement for the \n        CISCO-HARDWARE-IP-VERIFY-MIB.')
ciscoHardwareIpVerifyMIBStatisticGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 804, 2, 2, 1)).setObjects(("CISCO-HARDWARE-IP-VERIFY-MIB", "chivIpVerifyCheckStatus"), ("CISCO-HARDWARE-IP-VERIFY-MIB", "chivIpVerifyPacketsDropped"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoHardwareIpVerifyMIBStatisticGroup = ciscoHardwareIpVerifyMIBStatisticGroup.setStatus('current')
if mibBuilder.loadTexts: ciscoHardwareIpVerifyMIBStatisticGroup.setDescription('A collection of objects that provides configuration\n        and statistical information for IDS packet check.')
mibBuilder.exportSymbols("CISCO-HARDWARE-IP-VERIFY-MIB", chivIpVerifyTable=chivIpVerifyTable, ciscoHardwareIpVerifyMIBGroups=ciscoHardwareIpVerifyMIBGroups, ciscoHardwareIpVerifyMIBObjects=ciscoHardwareIpVerifyMIBObjects, ciscoHardwareIpVerifyMIBCompliance=ciscoHardwareIpVerifyMIBCompliance, ciscoHardwareIpVerifyMIB=ciscoHardwareIpVerifyMIB, ciscoHardwareIpVerifyMIBStatisticGroup=ciscoHardwareIpVerifyMIBStatisticGroup, ciscoHardwareIpVerifyMIBNotifs=ciscoHardwareIpVerifyMIBNotifs, PYSNMP_MODULE_ID=ciscoHardwareIpVerifyMIB, chivIpVerifyEntry=chivIpVerifyEntry, chivIpVerifyCheckTypeName=chivIpVerifyCheckTypeName, ciscoHardwareIpVerifyMIBConform=ciscoHardwareIpVerifyMIBConform, chivIpVerifyPacketsDropped=chivIpVerifyPacketsDropped, ciscoHardwareIpVerifyMIBCompliances=ciscoHardwareIpVerifyMIBCompliances, chivIpVerifyCheckIpType=chivIpVerifyCheckIpType, chivIpVerifyCheckStatus=chivIpVerifyCheckStatus)
