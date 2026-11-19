#
# PySNMP MIB module CISCO-NAT-EXT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-NAT-EXT-MIB
# Produced by pysmi-1.1.12 at Thu Nov 19 08:33:05 2026
# On host runnervmccnms platform Linux version 7.0.0-1019-azure by user runner
# Using Python version 3.11.18 (main, Oct 26 2026, 02:48:29) [GCC 15.2.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
entPhysicalIndex, = mibBuilder.importSymbols("ENTITY-MIB", "entPhysicalIndex")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
NotificationType, MibIdentifier, iso, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, ObjectIdentity, TimeTicks, IpAddress, Bits, Counter64, Gauge32, Unsigned32, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "MibIdentifier", "iso", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "ObjectIdentity", "TimeTicks", "IpAddress", "Bits", "Counter64", "Gauge32", "Unsigned32", "Counter32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoNATExtMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 532))
ciscoNATExtMIB.setRevisions(('2006-06-05 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoNATExtMIB.setRevisionsDescriptions(('Initial version of this MIB.',))
if mibBuilder.loadTexts: ciscoNATExtMIB.setLastUpdated('200606050000Z')
if mibBuilder.loadTexts: ciscoNATExtMIB.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoNATExtMIB.setContactInfo('       Cisco Systems\n                        Customer Service\n                        \n                Postal: 170 W Tasman Drive\n                        San Jose, CA  95134\n                        USA\n                        \n                   Tel: +1 800 553-NETS\n                   \n                E-mail:  cs-l4l7security@cisco.com')
if mibBuilder.loadTexts: ciscoNATExtMIB.setDescription('This MIB is an extension to the NAT-MIB.\n                 This MIB module includes objects for\n                 providing the NAT related statistics.\n                 \n                 Acronyms:\n                 \n                 NAT    Network Address Translation.\n                ')
ciscoNatExtMIBNotifs = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 532, 0))
ciscoNatExtMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 532, 1))
ciscoNatExtMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 532, 2))
cneAddrTranslationStatsTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 532, 1, 1), )
if mibBuilder.loadTexts: cneAddrTranslationStatsTable.setStatus('current')
if mibBuilder.loadTexts: cneAddrTranslationStatsTable.setDescription('A table of NAT statistics in a managed system.')
cneAddrTranslationStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 532, 1, 1, 1), ).setIndexNames((0, "ENTITY-MIB", "entPhysicalIndex"))
if mibBuilder.loadTexts: cneAddrTranslationStatsEntry.setStatus('current')
if mibBuilder.loadTexts: cneAddrTranslationStatsEntry.setDescription("An entry in the cneAddrTranslationStatsTable.\n                 This contains information about the NAT related\n                 statistics pertaining to a module.\n                 The entPhysicalIndex specifies the entry in \n                 entPhysicalTable with entPhysicalClass='module'.")
cneAddrTranslationNumActive = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 532, 1, 1, 1, 1), Gauge32()).setUnits('Number of address translation entries').setMaxAccess("readonly")
if mibBuilder.loadTexts: cneAddrTranslationNumActive.setReference('This object is an aggregate of the objects \n                 natAddrBindNumberOfEntries and\n                 natAddrPortBindNumberOfEntries defined in the \n                 RFC 4008, NAT-MIB [RFC4008].                \n                ')
if mibBuilder.loadTexts: cneAddrTranslationNumActive.setStatus('current')
if mibBuilder.loadTexts: cneAddrTranslationNumActive.setDescription('The total number of address translation entries that\n                 are currently available in the NAT device. This indicates\n                 the aggregate of the translation entries created from \n                 both the static and dynamic address translation \n                 mechanisms.\n                ')
cneAddrTranslationNumPeak = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 532, 1, 1, 1, 2), Unsigned32()).setUnits('Number of address translation entries').setMaxAccess("readonly")
if mibBuilder.loadTexts: cneAddrTranslationNumPeak.setStatus('current')
if mibBuilder.loadTexts: cneAddrTranslationNumPeak.setDescription('The maximum number of address translation entries\n                 that are active at any one time since the system\n                 startup. This indicates the high watermark of\n                 address translation entries that are active at any\n                 one time since the system startup.\n                 \n                 This object includes the translation entries created\n                 from both the static and dynamic address translation\n                 mechanisms.\n                ')
cneAddrTranslation1min = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 532, 1, 1, 1, 3), Gauge32()).setUnits('Address translation entries per second').setMaxAccess("readonly")
if mibBuilder.loadTexts: cneAddrTranslation1min.setStatus('current')
if mibBuilder.loadTexts: cneAddrTranslation1min.setDescription('The averaged number of address translation entries \n                 which the NAT device establishing per second, averaged\n                 over the last 1 minute.\n                 \n                 This object includes the translation entries created\n         from both the static and dynamic address translation\n                 mechanisms.\n                ')
cneAddrTranslation5min = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 532, 1, 1, 1, 4), Gauge32()).setUnits('Address translation entries per second').setMaxAccess("readonly")
if mibBuilder.loadTexts: cneAddrTranslation5min.setStatus('current')
if mibBuilder.loadTexts: cneAddrTranslation5min.setDescription('The averaged number of address translation entries which\n         the NAT device establishing per second, averaged over\n                 the last 5 minutes.\n                 \n         This object includes the translation entries created\n         from both the static and dynamic address translation\n                 mechanisms.\n                ')
ciscoNatExtMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 532, 2, 1))
ciscoNatExtMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 532, 2, 2))
ciscoNatExtMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 532, 2, 1, 1)).setObjects(("CISCO-NAT-EXT-MIB", "ciscoNatExtAddrTransStatsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoNatExtMIBCompliance = ciscoNatExtMIBCompliance.setStatus('current')
if mibBuilder.loadTexts: ciscoNatExtMIBCompliance.setDescription('The compliance statement for entities which implement the \n            CISCO-NAT-EXT-MIB.')
ciscoNatExtAddrTransStatsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 532, 2, 2, 1)).setObjects(("CISCO-NAT-EXT-MIB", "cneAddrTranslationNumActive"), ("CISCO-NAT-EXT-MIB", "cneAddrTranslationNumPeak"), ("CISCO-NAT-EXT-MIB", "cneAddrTranslation1min"), ("CISCO-NAT-EXT-MIB", "cneAddrTranslation5min"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoNatExtAddrTransStatsGroup = ciscoNatExtAddrTransStatsGroup.setStatus('current')
if mibBuilder.loadTexts: ciscoNatExtAddrTransStatsGroup.setDescription('This group contains the objects for NAT address translation \n           related statistics.')
mibBuilder.exportSymbols("CISCO-NAT-EXT-MIB", cneAddrTranslationNumPeak=cneAddrTranslationNumPeak, ciscoNATExtMIB=ciscoNATExtMIB, cneAddrTranslation5min=cneAddrTranslation5min, ciscoNatExtMIBConformance=ciscoNatExtMIBConformance, cneAddrTranslation1min=cneAddrTranslation1min, ciscoNatExtMIBCompliances=ciscoNatExtMIBCompliances, ciscoNatExtMIBNotifs=ciscoNatExtMIBNotifs, ciscoNatExtMIBGroups=ciscoNatExtMIBGroups, ciscoNatExtMIBCompliance=ciscoNatExtMIBCompliance, PYSNMP_MODULE_ID=ciscoNATExtMIB, ciscoNatExtMIBObjects=ciscoNatExtMIBObjects, cneAddrTranslationNumActive=cneAddrTranslationNumActive, cneAddrTranslationStatsTable=cneAddrTranslationStatsTable, cneAddrTranslationStatsEntry=cneAddrTranslationStatsEntry, ciscoNatExtAddrTransStatsGroup=ciscoNatExtAddrTransStatsGroup)
