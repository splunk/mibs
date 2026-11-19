#
# PySNMP MIB module DLB-GENERIC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/deliberant/DLB-GENERIC-MIB
# Produced by pysmi-1.1.12 at Thu Nov 19 08:33:27 2026
# On host runnervmccnms platform Linux version 7.0.0-1019-azure by user runner
# Using Python version 3.11.18 (main, Oct 26 2026, 02:48:29) [GCC 15.2.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint")
dlbMgmt, = mibBuilder.importSymbols("DELIBERANT-MIB", "dlbMgmt")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
sysLocation, = mibBuilder.importSymbols("SNMPv2-MIB", "sysLocation")
Unsigned32, Counter32, TimeTicks, ModuleIdentity, ObjectIdentity, iso, Integer32, MibIdentifier, IpAddress, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "Counter32", "TimeTicks", "ModuleIdentity", "ObjectIdentity", "iso", "Integer32", "MibIdentifier", "IpAddress", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
dlbGenericMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 32761, 3, 1))
dlbGenericMIB.setRevisions(('2009-02-13 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: dlbGenericMIB.setRevisionsDescriptions(('First revision.',))
if mibBuilder.loadTexts: dlbGenericMIB.setLastUpdated('200902130000Z')
if mibBuilder.loadTexts: dlbGenericMIB.setOrganization('Deliberant')
if mibBuilder.loadTexts: dlbGenericMIB.setContactInfo('\n        Deliberant Customer Support\n        E-mail: support@deliberant.com')
if mibBuilder.loadTexts: dlbGenericMIB.setDescription('The Deliberant Generic MIB.')
dlbGenericMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 32761, 3, 1, 1))
dlbGenericNotifs = MibIdentifier((1, 3, 6, 1, 4, 1, 32761, 3, 1, 1, 0))
dlbGenericInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 32761, 3, 1, 1, 1))
dlbPowerLoss = NotificationType((1, 3, 6, 1, 4, 1, 32761, 3, 1, 1, 0, 1)).setObjects(("SNMPv2-MIB", "sysLocation"))
if mibBuilder.loadTexts: dlbPowerLoss.setStatus('current')
if mibBuilder.loadTexts: dlbPowerLoss.setDescription('This notification is sent on device boot after power loss or device crash.')
dlbAdministrativeReboot = NotificationType((1, 3, 6, 1, 4, 1, 32761, 3, 1, 1, 0, 2)).setObjects(("SNMPv2-MIB", "sysLocation"))
if mibBuilder.loadTexts: dlbAdministrativeReboot.setStatus('current')
if mibBuilder.loadTexts: dlbAdministrativeReboot.setDescription('This notification is sent on device boot after administrator rebooted device.')
mibBuilder.exportSymbols("DLB-GENERIC-MIB", dlbPowerLoss=dlbPowerLoss, dlbGenericNotifs=dlbGenericNotifs, dlbGenericMIBObjects=dlbGenericMIBObjects, dlbAdministrativeReboot=dlbAdministrativeReboot, PYSNMP_MODULE_ID=dlbGenericMIB, dlbGenericMIB=dlbGenericMIB, dlbGenericInfo=dlbGenericInfo)
