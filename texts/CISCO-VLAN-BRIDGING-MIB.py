#
# PySNMP MIB module CISCO-VLAN-BRIDGING-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-VLAN-BRIDGING-MIB
# Produced by pysmi-1.1.12 at Thu Nov 26 06:07:44 2026
# On host runnervm0hi8g platform Linux version 7.0.0-1020-azure by user runner
# Using Python version 3.13.18 (main, Oct 26 2026, 14:19:33) [GCC 15.2.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
CiscoPortList, = mibBuilder.importSymbols("CISCO-TC", "CiscoPortList")
vtpVlanIndex, = mibBuilder.importSymbols("CISCO-VTP-MIB", "vtpVlanIndex")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, ModuleIdentity, TimeTicks, MibIdentifier, iso, Counter32, IpAddress, Integer32, NotificationType, ObjectIdentity, Unsigned32, Bits, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "ModuleIdentity", "TimeTicks", "MibIdentifier", "iso", "Counter32", "IpAddress", "Integer32", "NotificationType", "ObjectIdentity", "Unsigned32", "Bits", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ciscoVlanBridgingMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 56))
ciscoVlanBridgingMIB.setRevisions(('2003-08-22 00:00', '1996-09-12 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoVlanBridgingMIB.setRevisionsDescriptions(('Deprecate cvbStpForwardingMap and define\n             cvbStpForwardingMap2k to support up to 2k\n             bridge ports.', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoVlanBridgingMIB.setLastUpdated('200308220000Z')
if mibBuilder.loadTexts: ciscoVlanBridgingMIB.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoVlanBridgingMIB.setContactInfo('       Cisco Systems\n                    Customer Service\n\n            Postal: 170 W Tasman Drive\n                    San Jose, CA  95134\n                    USA\n\n               Tel: +1 800 553-NETS\n\n            E-mail: cs-vlans@cisco.com\n                    cs-lan-switch-snmp')
if mibBuilder.loadTexts: ciscoVlanBridgingMIB.setDescription('A set of managed objects for optimizing access to\n             bridging related data from RFC 1493.  This MIB is\n             modeled after portions of RFC 1493, adding VLAN ID\n             based indexing and bitmapped encoding of frequently\n             accessed data.')
ciscoVlanBridgingMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 56, 1))
cvbStp = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 56, 1, 1))
cvbStpTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 56, 1, 1, 1), )
if mibBuilder.loadTexts: cvbStpTable.setStatus('current')
if mibBuilder.loadTexts: cvbStpTable.setDescription('This table contains device STP status information\n            for each VLAN.')
cvbStpEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 56, 1, 1, 1, 1), ).setIndexNames((0, "CISCO-VTP-MIB", "vtpVlanIndex"))
if mibBuilder.loadTexts: cvbStpEntry.setStatus('current')
if mibBuilder.loadTexts: cvbStpEntry.setDescription('Device STP status for specified VLAN.')
cvbStpForwardingMap = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 56, 1, 1, 1, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 128))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cvbStpForwardingMap.setStatus('deprecated')
if mibBuilder.loadTexts: cvbStpForwardingMap.setDescription('An indication of which ports are forwarding by spanning \n            tree for the specified VLAN. The octet string contains\n            one bit per port on the bridge for the specified VLAN.\n\n            Each octet within the value of this object specifies a\n            set of eight ports, with the first octet specifying\n            ports 1 through 8, the second octet specifying ports 9\n            through 16, etc.   Within each octet, the most\n            significant bit represents the lowest numbered\n            port, and the least significant bit represents the\n            highest numbered port. \n\n            The bit value interpretation is related to RFC 1493\n            dot1dStpPortState values is as follows:\n               1 = forwarding\n               0 = disabled, blocking, listening, learning, broken, or\n                   nonexistent')
cvbStpForwardingMap2k = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 56, 1, 1, 1, 1, 3), CiscoPortList()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cvbStpForwardingMap2k.setStatus('current')
if mibBuilder.loadTexts: cvbStpForwardingMap2k.setDescription('An indication of which ports are forwarding by spanning \n            tree for the specified VLAN. The octet string contains\n            one bit per port on the bridge for the specified VLAN.\n            This object has STP status information of up to 2k ports\n            with the port number from 1 to 2048.\n\n            Each octet within the value of this object specifies a\n            set of eight ports, with the first octet specifying\n            ports 1 through 8, the second octet specifying ports 9\n            through 16, etc.   Within each octet, the most\n            significant bit represents the lowest numbered\n            port, and the least significant bit represents the\n            highest numbered port. \n\n            The bit value interpretation is related to RFC 1493\n            dot1dStpPortState values is as follows:\n               1 = forwarding\n               0 = disabled, blocking, listening, learning, broken, or\n                   nonexistent.')
ciscoVlanBridgingMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 56, 3))
ciscoVlanBridgingMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 56, 3, 1))
ciscoVlanBridgingMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 56, 3, 2))
ciscoVlanBridgingMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 56, 3, 1, 1)).setObjects(("CISCO-VLAN-BRIDGING-MIB", "ciscoVlanBridgingMIBGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoVlanBridgingMIBCompliance = ciscoVlanBridgingMIBCompliance.setStatus('deprecated')
if mibBuilder.loadTexts: ciscoVlanBridgingMIBCompliance.setDescription('The compliance statement for entities which implement\n            the Cisco VLAN Bridging MIB.')
ciscoVlanBridgingMIBCompliance2 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 56, 3, 1, 2)).setObjects(("CISCO-VLAN-BRIDGING-MIB", "ciscoVlanBridgingMIBGroup2"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoVlanBridgingMIBCompliance2 = ciscoVlanBridgingMIBCompliance2.setStatus('current')
if mibBuilder.loadTexts: ciscoVlanBridgingMIBCompliance2.setDescription('The compliance statement for entities which implement\n            the Cisco VLAN Bridging MIB.')
ciscoVlanBridgingMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 56, 3, 2, 1)).setObjects(("CISCO-VLAN-BRIDGING-MIB", "cvbStpForwardingMap"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoVlanBridgingMIBGroup = ciscoVlanBridgingMIBGroup.setStatus('deprecated')
if mibBuilder.loadTexts: ciscoVlanBridgingMIBGroup.setDescription('A collection of objects providing the STP status \n            information of up to 1k ports with the port number \n            from 1 to 1024.')
ciscoVlanBridgingMIBGroup2 = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 56, 3, 2, 2)).setObjects(("CISCO-VLAN-BRIDGING-MIB", "cvbStpForwardingMap2k"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoVlanBridgingMIBGroup2 = ciscoVlanBridgingMIBGroup2.setStatus('current')
if mibBuilder.loadTexts: ciscoVlanBridgingMIBGroup2.setDescription('A collection of objects providing the STP status \n            information of up to 2k ports with the port number \n            from 1 to 2048.')
mibBuilder.exportSymbols("CISCO-VLAN-BRIDGING-MIB", cvbStpForwardingMap2k=cvbStpForwardingMap2k, ciscoVlanBridgingMIBConformance=ciscoVlanBridgingMIBConformance, cvbStpForwardingMap=cvbStpForwardingMap, cvbStpTable=cvbStpTable, cvbStpEntry=cvbStpEntry, ciscoVlanBridgingMIBCompliances=ciscoVlanBridgingMIBCompliances, ciscoVlanBridgingMIBGroup=ciscoVlanBridgingMIBGroup, ciscoVlanBridgingMIBGroups=ciscoVlanBridgingMIBGroups, ciscoVlanBridgingMIBCompliance2=ciscoVlanBridgingMIBCompliance2, ciscoVlanBridgingMIB=ciscoVlanBridgingMIB, cvbStp=cvbStp, PYSNMP_MODULE_ID=ciscoVlanBridgingMIB, ciscoVlanBridgingMIBObjects=ciscoVlanBridgingMIBObjects, ciscoVlanBridgingMIBGroup2=ciscoVlanBridgingMIBGroup2, ciscoVlanBridgingMIBCompliance=ciscoVlanBridgingMIBCompliance)
