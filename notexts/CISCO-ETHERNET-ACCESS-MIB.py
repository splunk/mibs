#
# PySNMP MIB module CISCO-ETHERNET-ACCESS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-ETHERNET-ACCESS-MIB
# Produced by pysmi-1.1.12 at Thu Nov 26 06:06:57 2026
# On host runnervm0hi8g platform Linux version 7.0.0-1020-azure by user runner
# Using Python version 3.13.18 (main, Oct 26 2026, 14:19:33) [GCC 15.2.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
managementDomainIndex, vtpVlanIndex = mibBuilder.importSymbols("CISCO-VTP-MIB", "managementDomainIndex", "vtpVlanIndex")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
Counter64, TimeTicks, NotificationType, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, ModuleIdentity, IpAddress, Bits, Gauge32, Unsigned32, MibIdentifier, Counter32, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "TimeTicks", "NotificationType", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "ModuleIdentity", "IpAddress", "Bits", "Gauge32", "Unsigned32", "MibIdentifier", "Counter32", "ObjectIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoEthernetAccessMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 466))
ciscoEthernetAccessMIB.setRevisions(('2007-09-14 00:00', '2005-01-18 00:00',))
if mibBuilder.loadTexts: ciscoEthernetAccessMIB.setLastUpdated('200709140000Z')
if mibBuilder.loadTexts: ciscoEthernetAccessMIB.setOrganization('Cisco Systems, Inc.')
ciscoEthernetAccessMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 466, 1))
ciscoEthernetAccessMIBConform = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 466, 2))
ceaGlobals = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 466, 1, 1))
ceaConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 466, 1, 2))
class CeaVlanUNIType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("other", 1), ("isolated", 2), ("community", 3))

ceaMaxNNIPorts = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 466, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 512))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ceaMaxNNIPorts.setStatus('current')
ceaMaxUNIVlanCommunityPorts = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 466, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 512))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ceaMaxUNIVlanCommunityPorts.setStatus('current')
ceaPortTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 466, 1, 2, 1), )
if mibBuilder.loadTexts: ceaPortTable.setStatus('current')
ceaPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 466, 1, 2, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: ceaPortEntry.setStatus('current')
ceaPortType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 466, 1, 2, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("unspecified", 1), ("uni", 2), ("nni", 3), ("eni", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ceaPortType.setStatus('current')
ceaPortCapability = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 466, 1, 2, 1, 1, 2), Bits().clone(namedValues=NamedValues(("nni", 0), ("uni", 1), ("eni", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ceaPortCapability.setStatus('current')
ceaUNIVlanTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 466, 1, 2, 2), )
if mibBuilder.loadTexts: ceaUNIVlanTable.setStatus('current')
ceaUNIVlanEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 466, 1, 2, 2, 1), ).setIndexNames((0, "CISCO-VTP-MIB", "managementDomainIndex"), (0, "CISCO-VTP-MIB", "vtpVlanIndex"))
if mibBuilder.loadTexts: ceaUNIVlanEntry.setStatus('current')
ceaUNIVlanType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 466, 1, 2, 2, 1, 1), CeaVlanUNIType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ceaUNIVlanType.setStatus('current')
cEthernetAccessMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 466, 2, 1))
cEthernetAccessMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 466, 2, 2))
cEthernetAccessMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 466, 2, 1, 1)).setObjects(("CISCO-ETHERNET-ACCESS-MIB", "ceaPortGroup"), ("CISCO-ETHERNET-ACCESS-MIB", "ceaVlanGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cEthernetAccessMIBCompliance = cEthernetAccessMIBCompliance.setStatus('current')
ceaPortGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 466, 2, 2, 1)).setObjects(("CISCO-ETHERNET-ACCESS-MIB", "ceaMaxNNIPorts"), ("CISCO-ETHERNET-ACCESS-MIB", "ceaPortType"), ("CISCO-ETHERNET-ACCESS-MIB", "ceaPortCapability"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ceaPortGroup = ceaPortGroup.setStatus('current')
ceaVlanGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 466, 2, 2, 2)).setObjects(("CISCO-ETHERNET-ACCESS-MIB", "ceaMaxUNIVlanCommunityPorts"), ("CISCO-ETHERNET-ACCESS-MIB", "ceaUNIVlanType"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ceaVlanGroup = ceaVlanGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-ETHERNET-ACCESS-MIB", CeaVlanUNIType=CeaVlanUNIType, cEthernetAccessMIBCompliances=cEthernetAccessMIBCompliances, ceaMaxNNIPorts=ceaMaxNNIPorts, ceaPortType=ceaPortType, ciscoEthernetAccessMIB=ciscoEthernetAccessMIB, ciscoEthernetAccessMIBObjects=ciscoEthernetAccessMIBObjects, ceaMaxUNIVlanCommunityPorts=ceaMaxUNIVlanCommunityPorts, ceaGlobals=ceaGlobals, ciscoEthernetAccessMIBConform=ciscoEthernetAccessMIBConform, ceaConfig=ceaConfig, ceaPortCapability=ceaPortCapability, ceaPortGroup=ceaPortGroup, PYSNMP_MODULE_ID=ciscoEthernetAccessMIB, cEthernetAccessMIBGroups=cEthernetAccessMIBGroups, ceaUNIVlanTable=ceaUNIVlanTable, ceaUNIVlanType=ceaUNIVlanType, ceaUNIVlanEntry=ceaUNIVlanEntry, ceaPortEntry=ceaPortEntry, ceaPortTable=ceaPortTable, cEthernetAccessMIBCompliance=cEthernetAccessMIBCompliance, ceaVlanGroup=ceaVlanGroup)
