#
# PySNMP MIB module CISCO-SNMP-HANDSHAKE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-SNMP-HANDSHAKE-MIB
# Produced by pysmi-1.1.12 at Thu Nov 26 06:07:44 2026
# On host runnervm0hi8g platform Linux version 7.0.0-1020-azure by user runner
# Using Python version 3.13.18 (main, Oct 26 2026, 14:19:33) [GCC 15.2.0]
#
bsnWireless, = mibBuilder.importSymbols("AIRESPACE-WIRELESS-MIB", "bsnWireless")
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, ModuleIdentity, TimeTicks, MibIdentifier, iso, Counter32, IpAddress, Integer32, NotificationType, ObjectIdentity, Unsigned32, Bits, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "ModuleIdentity", "TimeTicks", "MibIdentifier", "iso", "Counter32", "IpAddress", "Integer32", "NotificationType", "ObjectIdentity", "Unsigned32", "Bits", "Gauge32")
TextualConvention, DisplayString, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString", "TruthValue")
ciscoSnmpHandshakeMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 14179, 2, 40))
ciscoSnmpHandshakeMIB.setRevisions(('2007-05-23 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoSnmpHandshakeMIB.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoSnmpHandshakeMIB.setLastUpdated('200705230000Z')
if mibBuilder.loadTexts: ciscoSnmpHandshakeMIB.setOrganization('Cisco Systems Inc.')
if mibBuilder.loadTexts: ciscoSnmpHandshakeMIB.setContactInfo('        Cisco Systems,\n                        Customer Service\n\n                Postal: 170 West Tasman Drive\n                        San Jose, CA  95134\n                        USA\n\n                   Tel: +1 800 553-NETS\n\n                 Email: cs-wnbu-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoSnmpHandshakeMIB.setDescription('This MIB is intended for those devices where\n               SNMP access is given to be given to known SNMP \n               Manager only. All the SNMP MIBs are published, \n               any thrid party SNMP browser can retrieve data \n               using SNMP protocol. By implementing this MIB, a\n               application layer handshake has to be done before \n               any MIB view access is granted to SNMPV2c community \n               string or SNMPV3 user. \n               \n               Once the handshake is successfully over then SNMP \n               agent can create VACM entry to provide access to any\n               MIB view. \n               \n                                  GLOSSARY\n                \n               View-based Access Control Model ( VACM )\n               \n               The VACM determines whether access to a managed \n               object in a local MIB by a remote SNMP manager \n               should be allowed.')
ciscoSnmpHandshakeMIBNotifs = MibIdentifier((1, 3, 6, 1, 4, 1, 14179, 2, 40, 0))
ciscoSnmpHandshakeMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 14179, 2, 40, 1))
ciscoSnmpHandshakeMIBConform = MibIdentifier((1, 3, 6, 1, 4, 1, 14179, 2, 40, 2))
ciscoSnmpHandshakeProcess = MibIdentifier((1, 3, 6, 1, 4, 1, 14179, 2, 40, 1, 1))
ciscoSnmpHandshakeTest = MibIdentifier((1, 3, 6, 1, 4, 1, 14179, 2, 40, 1, 2))
csHandshakeInit = MibScalar((1, 3, 6, 1, 4, 1, 14179, 2, 40, 1, 1, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(16, 16)).setFixedLength(16)).setMaxAccess("readonly")
if mibBuilder.loadTexts: csHandshakeInit.setStatus('current')
if mibBuilder.loadTexts: csHandshakeInit.setDescription('Get on this object will return random 16 bytes\n                octet-string. Device will cache this string against\n                IP-Address of sender. This string will be later used\n                to comeplete the handshake.')
csHandshakeUpdate = MibScalar((1, 3, 6, 1, 4, 1, 14179, 2, 40, 1, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(16, 16)).setFixedLength(16)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: csHandshakeUpdate.setStatus('current')
if mibBuilder.loadTexts: csHandshakeUpdate.setDescription("Set on this object will make snmp agent to run \n                the secret algorithm to give access or deny access \n                to SNMP manager. Access will be given to the community\n                string used and to the sender's IP-Address only.")
csHandshakeCheck = MibScalar((1, 3, 6, 1, 4, 1, 14179, 2, 40, 1, 2, 1), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: csHandshakeCheck.setStatus('current')
if mibBuilder.loadTexts: csHandshakeCheck.setDescription('This object can be use to perform test of MIB \n                view access. Once the handshake is successfully \n                completed. The MIB-view access will be granted \n                for this object, If MIB-view is not granted yet \n                for this object then no-access error will be \n                returned.')
ciscoSnmpHandshakeMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 14179, 2, 40, 2, 1))
ciscoSnmpHandshakeMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 14179, 2, 40, 2, 2))
ciscoSnmpHandshakeMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 14179, 2, 40, 2, 1, 1)).setObjects(("CISCO-SNMP-HANDSHAKE-MIB", "ciscoSnmpHandshakeGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSnmpHandshakeMIBCompliance = ciscoSnmpHandshakeMIBCompliance.setStatus('current')
if mibBuilder.loadTexts: ciscoSnmpHandshakeMIBCompliance.setDescription('The compliance statement for the SNMP entities \n                 that implement the ciscoSnmpHandshakeMIB module.')
ciscoSnmpHandshakeGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 14179, 2, 40, 2, 2, 1)).setObjects(("CISCO-SNMP-HANDSHAKE-MIB", "csHandshakeInit"), ("CISCO-SNMP-HANDSHAKE-MIB", "csHandshakeUpdate"), ("CISCO-SNMP-HANDSHAKE-MIB", "csHandshakeCheck"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSnmpHandshakeGroup = ciscoSnmpHandshakeGroup.setStatus('current')
if mibBuilder.loadTexts: ciscoSnmpHandshakeGroup.setDescription('This collection of objects represents the \n                 information about attributes needed to completed\n                 SNMP handhshake')
mibBuilder.exportSymbols("CISCO-SNMP-HANDSHAKE-MIB", ciscoSnmpHandshakeMIBCompliance=ciscoSnmpHandshakeMIBCompliance, csHandshakeInit=csHandshakeInit, ciscoSnmpHandshakeProcess=ciscoSnmpHandshakeProcess, ciscoSnmpHandshakeMIBCompliances=ciscoSnmpHandshakeMIBCompliances, csHandshakeCheck=csHandshakeCheck, ciscoSnmpHandshakeGroup=ciscoSnmpHandshakeGroup, ciscoSnmpHandshakeMIB=ciscoSnmpHandshakeMIB, ciscoSnmpHandshakeMIBGroups=ciscoSnmpHandshakeMIBGroups, PYSNMP_MODULE_ID=ciscoSnmpHandshakeMIB, ciscoSnmpHandshakeMIBConform=ciscoSnmpHandshakeMIBConform, ciscoSnmpHandshakeTest=ciscoSnmpHandshakeTest, ciscoSnmpHandshakeMIBObjects=ciscoSnmpHandshakeMIBObjects, csHandshakeUpdate=csHandshakeUpdate, ciscoSnmpHandshakeMIBNotifs=ciscoSnmpHandshakeMIBNotifs)
