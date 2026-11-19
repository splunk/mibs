#
# PySNMP MIB module CISCO-VLAN-IFTABLE-RELATIONSHIP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-VLAN-IFTABLE-RELATIONSHIP-MIB
# Produced by pysmi-1.1.12 at Thu Nov 19 14:35:14 2026
# On host runnervmccnms platform Linux version 7.0.0-1019-azure by user runner
# Using Python version 3.11.18 (main, Oct 26 2026, 02:48:29) [GCC 15.2.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
InterfaceIndexOrZero, = mibBuilder.importSymbols("CISCO-TC", "InterfaceIndexOrZero")
VlanIndex, = mibBuilder.importSymbols("CISCO-VTP-MIB", "VlanIndex")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, Integer32, Gauge32, MibIdentifier, NotificationType, Unsigned32, Counter64, ObjectIdentity, IpAddress, iso, Counter32, ModuleIdentity, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "Integer32", "Gauge32", "MibIdentifier", "NotificationType", "Unsigned32", "Counter64", "ObjectIdentity", "IpAddress", "iso", "Counter32", "ModuleIdentity", "TimeTicks")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoVlanIfTableRelationshipMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 128))
ciscoVlanIfTableRelationshipMIB.setRevisions(('2013-07-15 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoVlanIfTableRelationshipMIB.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoVlanIfTableRelationshipMIB.setLastUpdated('9904010530Z')
if mibBuilder.loadTexts: ciscoVlanIfTableRelationshipMIB.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoVlanIfTableRelationshipMIB.setContactInfo('Cisco Systems\n            Customer Service\n\n            Postal: 170 W Tasman Drive\n                    San Jose, CA  95134\n                    USA\n\n            Tel: +1 800 553-NETS\n\n            E-mail: cs-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoVlanIfTableRelationshipMIB.setDescription("Cisco VLAN ifTable Relationship MIB lists VLAN-id and ifIndex\n        information for routed VLAN interfaces.  \n\n        A routed VLAN interface is the router interface or sub-interface \n        to which the router's IP address on the VLAN is attached.  \n        For example, an ISL, SDE, or 802.1Q encapsulated\n        subinterface, or Switched Virtual Interface (SVI).")
cviMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 128, 1))
cviGlobals = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 128, 1, 1))
cviVlanInterfaceIndexTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 128, 1, 1, 1), )
if mibBuilder.loadTexts: cviVlanInterfaceIndexTable.setStatus('current')
if mibBuilder.loadTexts: cviVlanInterfaceIndexTable.setDescription("The cviVlanInterfaceIndexTable provides a way to\n        translate a VLAN-id in to an ifIndex, so that \n        the routed VLAN interface's routing configuration \n        can be obtained from interface entry in ipRouteTable.\n\n        Note that some routers can have interfaces to multiple\n        VLAN management domains, and therefore can have multiple \n        routed VLAN interfaces which connect to different VLANs \n        having the same VLAN-id.  Thus, it is possible to have \n        multiple rows in this table for the same VLAN-id.\n\n        The cviVlanInterfaceIndexTable also provides a way\n        to find the VLAN-id from an ifTable VLAN's ifIndex.")
cviVlanInterfaceIndexEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 128, 1, 1, 1, 1), ).setIndexNames((0, "CISCO-VLAN-IFTABLE-RELATIONSHIP-MIB", "cviVlanId"), (0, "CISCO-VLAN-IFTABLE-RELATIONSHIP-MIB", "cviPhysicalIfIndex"))
if mibBuilder.loadTexts: cviVlanInterfaceIndexEntry.setStatus('current')
if mibBuilder.loadTexts: cviVlanInterfaceIndexEntry.setDescription('Each entry represents a routed VLAN interface, its\n        corresponding physical port if any, and the ifTable entry\n        for the routed VLAN interface.\n\n        Entries are created by the agent when the routed VLAN interface\n        is created.  Operational status of routing does not affect\n        the entries listed here.  For routing configuration please refer\n        to ipRouteTable.\n\n        Entries are deleted by the agent when the routed VLAN interface\n        is removed from the system configuration.')
cviVlanId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 128, 1, 1, 1, 1, 1), VlanIndex())
if mibBuilder.loadTexts: cviVlanId.setStatus('current')
if mibBuilder.loadTexts: cviVlanId.setDescription('The VLAN-id number of the routed VLAN interface.')
cviPhysicalIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 128, 1, 1, 1, 1, 2), InterfaceIndexOrZero())
if mibBuilder.loadTexts: cviPhysicalIfIndex.setStatus('current')
if mibBuilder.loadTexts: cviPhysicalIfIndex.setDescription('For subinterfaces, this object is the ifIndex of the\n        physical interface for the subinterface.\n\n        For Switch Virtual Interfaces (SVIs), this object is zero.')
cviRoutedVlanIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 128, 1, 1, 1, 1, 3), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cviRoutedVlanIfIndex.setStatus('current')
if mibBuilder.loadTexts: cviRoutedVlanIfIndex.setDescription('The index for the ifTable entry associated with\n        this routed VLAN interface.')
cviMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 128, 1, 3))
cviMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 128, 1, 3, 1))
cviMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 128, 1, 3, 2))
cviMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 128, 1, 3, 1, 1)).setObjects(("CISCO-VLAN-IFTABLE-RELATIONSHIP-MIB", "cviMIBGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cviMIBCompliance = cviMIBCompliance.setStatus('current')
if mibBuilder.loadTexts: cviMIBCompliance.setDescription('The compliance statement for entities which implement\n        the CISCO-VLAN-INTERFACE-MIB')
cviMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 128, 1, 3, 2, 1)).setObjects(("CISCO-VLAN-IFTABLE-RELATIONSHIP-MIB", "cviRoutedVlanIfIndex"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cviMIBGroup = cviMIBGroup.setStatus('current')
if mibBuilder.loadTexts: cviMIBGroup.setDescription('A set of objects to obtain VLAN-ID and ifIndex\n        information for routed VLAN interfaces.')
mibBuilder.exportSymbols("CISCO-VLAN-IFTABLE-RELATIONSHIP-MIB", cviMIBGroups=cviMIBGroups, PYSNMP_MODULE_ID=ciscoVlanIfTableRelationshipMIB, cviPhysicalIfIndex=cviPhysicalIfIndex, ciscoVlanIfTableRelationshipMIB=ciscoVlanIfTableRelationshipMIB, cviMIBGroup=cviMIBGroup, cviMIBCompliance=cviMIBCompliance, cviVlanId=cviVlanId, cviVlanInterfaceIndexTable=cviVlanInterfaceIndexTable, cviRoutedVlanIfIndex=cviRoutedVlanIfIndex, cviMIBCompliances=cviMIBCompliances, cviMIBObjects=cviMIBObjects, cviGlobals=cviGlobals, cviMIBConformance=cviMIBConformance, cviVlanInterfaceIndexEntry=cviVlanInterfaceIndexEntry)
