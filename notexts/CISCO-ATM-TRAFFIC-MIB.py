#
# PySNMP MIB module CISCO-ATM-TRAFFIC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-ATM-TRAFFIC-MIB
# Produced by pysmi-1.1.12 at Thu Nov 26 06:06:59 2026
# On host runnervm0hi8g platform Linux version 7.0.0-1020-azure by user runner
# Using Python version 3.13.18 (main, Oct 26 2026, 14:19:33) [GCC 15.2.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
atmTrafficDescrParamEntry, = mibBuilder.importSymbols("ATM-MIB", "atmTrafficDescrParamEntry")
ciscoExperiment, = mibBuilder.importSymbols("CISCO-SMI", "ciscoExperiment")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
Counter64, TimeTicks, NotificationType, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, ModuleIdentity, IpAddress, Bits, Gauge32, Unsigned32, MibIdentifier, Counter32, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "TimeTicks", "NotificationType", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "ModuleIdentity", "IpAddress", "Bits", "Gauge32", "Unsigned32", "MibIdentifier", "Counter32", "ObjectIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoAtmTrafficExtMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 10, 11))
ciscoAtmTrafficExtMIB.setRevisions(('2002-08-26 00:00', '2001-11-01 00:00', '1997-05-29 00:00',))
if mibBuilder.loadTexts: ciscoAtmTrafficExtMIB.setLastUpdated('200208260000Z')
if mibBuilder.loadTexts: ciscoAtmTrafficExtMIB.setOrganization('Cisco System Inc.')
ciscoAtmTrafficExtMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 11, 1))
ciscoAtmTrafficTypeExt = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 11, 1, 1))
ciscoAtmTrafficTableExt = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 11, 1, 2))
atmNoClpNoScrCdvt = ObjectIdentity((1, 3, 6, 1, 4, 1, 9, 10, 11, 1, 1, 1))
if mibBuilder.loadTexts: atmNoClpNoScrCdvt.setStatus('deprecated')
atmClpScrMbsCdvt = ObjectIdentity((1, 3, 6, 1, 4, 1, 9, 10, 11, 1, 1, 2))
if mibBuilder.loadTexts: atmClpScrMbsCdvt.setStatus('current')
atmNoClpScrMbsCdvt = ObjectIdentity((1, 3, 6, 1, 4, 1, 9, 10, 11, 1, 1, 3))
if mibBuilder.loadTexts: atmNoClpScrMbsCdvt.setStatus('current')
atmNoClpMcr = ObjectIdentity((1, 3, 6, 1, 4, 1, 9, 10, 11, 1, 1, 4))
if mibBuilder.loadTexts: atmNoClpMcr.setStatus('current')
atmNoClpMcrCdvt = ObjectIdentity((1, 3, 6, 1, 4, 1, 9, 10, 11, 1, 1, 5))
if mibBuilder.loadTexts: atmNoClpMcrCdvt.setStatus('current')
atmTrafficDescrParamExtTable = MibTable((1, 3, 6, 1, 4, 1, 9, 10, 11, 1, 2, 1), )
if mibBuilder.loadTexts: atmTrafficDescrParamExtTable.setStatus('current')
atmTrafficDescrParamExtEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 10, 11, 1, 2, 1, 1), )
atmTrafficDescrParamEntry.registerAugmentions(("CISCO-ATM-TRAFFIC-MIB", "atmTrafficDescrParamExtEntry"))
atmTrafficDescrParamExtEntry.setIndexNames(*atmTrafficDescrParamEntry.getIndexNames())
if mibBuilder.loadTexts: atmTrafficDescrParamExtEntry.setStatus('current')
atmTrafficExplicitServCategory = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 11, 1, 2, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("cbr", 1), ("vbrRt", 2), ("vbrNrt", 3), ("abr", 4), ("ubr", 5), ("notDef", 6))).clone('notDef')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: atmTrafficExplicitServCategory.setStatus('current')
atmTrafficDerivedServCategory = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 11, 1, 2, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("cbr", 1), ("vbrRt", 2), ("vbrNrt", 3), ("abr", 4), ("ubr", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmTrafficDerivedServCategory.setStatus('current')
atmTrafficDescriptorName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 11, 1, 2, 1, 1, 3), SnmpAdminString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: atmTrafficDescriptorName.setStatus('current')
ciscoAtmTrafficExtMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 11, 3))
ciscoAtmTrafficExtMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 11, 3, 1))
ciscoAtmTrafficExtMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 11, 3, 2))
ciscoAtmTrafficExtMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 10, 11, 3, 1, 1)).setObjects(("CISCO-ATM-TRAFFIC-MIB", "ciscoAtmTrafficTableExtMIBGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoAtmTrafficExtMIBCompliance = ciscoAtmTrafficExtMIBCompliance.setStatus('deprecated')
ciscoAtmTrafficExtMIBComplianceRev1 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 10, 11, 3, 1, 2)).setObjects(("CISCO-ATM-TRAFFIC-MIB", "ciscoAtmTrafficTableExtMIBGroup"), ("CISCO-ATM-TRAFFIC-MIB", "ciscoAtmTrafficNmsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoAtmTrafficExtMIBComplianceRev1 = ciscoAtmTrafficExtMIBComplianceRev1.setStatus('current')
ciscoAtmTrafficTableExtMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 10, 11, 3, 2, 1)).setObjects(("CISCO-ATM-TRAFFIC-MIB", "atmTrafficExplicitServCategory"), ("CISCO-ATM-TRAFFIC-MIB", "atmTrafficDerivedServCategory"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoAtmTrafficTableExtMIBGroup = ciscoAtmTrafficTableExtMIBGroup.setStatus('current')
ciscoAtmTrafficNmsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 10, 11, 3, 2, 2)).setObjects(("CISCO-ATM-TRAFFIC-MIB", "atmTrafficDescriptorName"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoAtmTrafficNmsGroup = ciscoAtmTrafficNmsGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-ATM-TRAFFIC-MIB", atmTrafficDerivedServCategory=atmTrafficDerivedServCategory, atmNoClpScrMbsCdvt=atmNoClpScrMbsCdvt, atmNoClpMcr=atmNoClpMcr, ciscoAtmTrafficExtMIB=ciscoAtmTrafficExtMIB, atmTrafficDescrParamExtTable=atmTrafficDescrParamExtTable, ciscoAtmTrafficTypeExt=ciscoAtmTrafficTypeExt, PYSNMP_MODULE_ID=ciscoAtmTrafficExtMIB, atmNoClpNoScrCdvt=atmNoClpNoScrCdvt, atmTrafficDescriptorName=atmTrafficDescriptorName, ciscoAtmTrafficNmsGroup=ciscoAtmTrafficNmsGroup, atmClpScrMbsCdvt=atmClpScrMbsCdvt, ciscoAtmTrafficExtMIBConformance=ciscoAtmTrafficExtMIBConformance, ciscoAtmTrafficExtMIBCompliance=ciscoAtmTrafficExtMIBCompliance, ciscoAtmTrafficExtMIBComplianceRev1=ciscoAtmTrafficExtMIBComplianceRev1, ciscoAtmTrafficExtMIBCompliances=ciscoAtmTrafficExtMIBCompliances, ciscoAtmTrafficExtMIBGroups=ciscoAtmTrafficExtMIBGroups, atmTrafficExplicitServCategory=atmTrafficExplicitServCategory, atmTrafficDescrParamExtEntry=atmTrafficDescrParamExtEntry, ciscoAtmTrafficTableExt=ciscoAtmTrafficTableExt, ciscoAtmTrafficExtMIBObjects=ciscoAtmTrafficExtMIBObjects, atmNoClpMcrCdvt=atmNoClpMcrCdvt, ciscoAtmTrafficTableExtMIBGroup=ciscoAtmTrafficTableExtMIBGroup)
